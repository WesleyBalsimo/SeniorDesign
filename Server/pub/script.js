// ------------------------ WEBSOCKET HANDLERS ------------------------
var ws = null

function setupWebSockets(reconnect_time) {
  let reconnect_delay = reconnect_time;

  console.log("Attempting to connect websocket...");

  const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
  ws = new WebSocket(`${protocol}//${window.location.host}/ws`);
  ws.binaryType = "arraybuffer";

  ws.onopen = () => {
    console.log("Connceted to websocket.");
    reconnect_delay = 1000;
  };

  ws.onmessage = (event) => {
    const view = new DataView(event.data);
    const packet_id = view.getUint8(0);
    if (packet_id == 0x00) {
      const queue_position = view.getUint8(1);
      alert(`Oops, someone is already using the robot right now! Current queue positon: ${queue_position}`);
    } else if (packet_id == 0x01) {
      alert("Moving the robot to your part's location!");
    } else if (packet_id == 0x02) {
      alert("Password was incorrect! Please try again later.");
    } else if (packet_id == 0x03) {
      alert("CSV has been successfully updated!");
    } else if (packet_id == 0x04) {
      const invalid_line = view.getUint16(1);
      alert(`CSV has invalid syntax on line (${invalid_line}). Make sure you are just exporting the execl sheet!`);
    } else {
      alert("An unexpected error has occured! Please try again soon!");
    }
  };

  ws.onerror = (error) => {
    console.error(error);
  };

  ws.onclose = () => {
    console.log("Attempting to reconnect in " + reconnect_delay + "ms...");
    setTimeout(() => setupWebSockets(reconnect_delay * 2), reconnect_delay);
  };
}
setupWebSockets(500);

// ------------------------ SETUP HOME ------------------------
const homeElement = document.getElementById("home");
function showHome() {
  const elements = document.getElementById("categories");
  for (const c of elements.childNodes) {
    if (c.nodeName != "H2" || !c.classList.contains("active")) continue;
    c.classList.remove("active");
    document.getElementsByClassName(`category-${c.innerHTML.replace(" ", "-")}`)[0].hidden = true;
    break;
  }
  homeElement.classList.add("active");
  document.getElementsByClassName(`category-Home`)[0].hidden = false;
}
showHome();

// ------------------------ CSV HANDLERS ------------------------
async function getCsv() {
  const response = await fetch("static/data.csv");

  if (!response.ok)
    throw new Error(`Response status: ${response.status}`);

  const result = await response.text();
  return result.trim().split("\n").map(r => r.split(","));
}

function csvToCategories(csv) {
  const [header, ...data] = csv;
  const categories = {};

  for (const row of data) {
    if (!(row[0] in categories)) {
      categories[row[0]] = [];
    }

    categories[row[0]].push(row.slice(1));
  }

  return categories;
}

async function getCategories() {
  const csv = getCsv();
  return csvToCategories(await csv);
}

async function updateCSV() {
  const input = document.getElementById("updateInput");
  const file = input.files[0];
  if (!file) {
    alert("You must supply a csv file to update the inventory!");
    return;
  }

  const password = prompt("Enter admin password:");
  if (!password) {
    alert("You must enter a password to update the inventory!");
    return;
  }

  const csv = await file.text();

  const encoder = new TextEncoder();

  const passwordBytes = encoder.encode(password);
  const csvBytes = encoder.encode(csv);

  const buffer = new Uint8Array(2 + passwordBytes.length + csvBytes.length);

  buffer[0] = 0x01;
  buffer[1] = passwordBytes.length;
  buffer.set(passwordBytes, 2);
  buffer.set(csvBytes, 2 + passwordBytes.length);

  ws.send(buffer);

  window.location.reload(); // Reload to update the UI with new items, and to reset the input
}

// ------------------------ UPDATING DOM WITH CATEGORIES ------------------------
function create(htmlStr) {
  var frag = document.createDocumentFragment(),
    temp = document.createElement('div');
  temp.innerHTML = htmlStr;
  while (temp.firstChild) {
    frag.appendChild(temp.firstChild);
  }
  return frag;
}

function selectItem(location_raw) {
  item_location = location_raw.trim();
  console.log("Selected item '" + item_location + `' (${item_location.length})`);
  if (item_location.length !== 2) {
    alert("This item's location has been configured incorrectly! Contact the administrator to fix the issue.");
  }
  var buffer = new ArrayBuffer(3);
  var view = new DataView(buffer);
  view.setUint8(0, 0x00);
  view.setUint8(1, item_location.charCodeAt(0));
  view.setUint8(2, item_location.charCodeAt(1));
  ws.send(buffer);
}

function addCategory(name, items) {
  const categoryClassName = name.replace(" ", "-");
  var categoryElement = document.createElement("h2");
  categoryElement.innerHTML = name;
  categoryElement.classList.add("category");
  categoryElement.onclick = () => {
    const elements = document.getElementById("categories");
    for (const c of elements.childNodes) {
      if (c.nodeName != "H2" || !c.classList.contains("active")) continue;
      c.classList.remove("active");
      document.getElementsByClassName(`category-${c.innerHTML.replace(" ", "-")}`)[0].hidden = true;
      break;
    }
    categoryElement.classList.add("active");

    document.getElementsByClassName(`category-${categoryClassName}`)[0].hidden = false;
  };
  document.getElementById("categories").appendChild(categoryElement);

  var categoryItems = document.createElement("div");
  categoryItems.className = "category-" + categoryClassName;
  categoryItems.hidden = true;

  for (const item of items) {
    const button = document.createElement("button");
    button.onclick = () => selectItem(item[1]);
    const img = document.createElement('img');
    if (name == "Resistor") {
      colorResistor(img, item[0]);
    } else {
      img.src = `/images/${name}.svg`;
      img.onerror = function() {
        this.onerror = null;
        this.src = "/images/Component.svg";
      };
      img.alt = name;
    }
    const span = document.createElement('span');
    span.textContent = item[0];

    button.appendChild(img);
    button.appendChild(span);

    categoryItems.appendChild(button);
  }

  document.getElementById("items").appendChild(categoryItems);
}

getCategories().then(data => {
  for (const [category, items] of Object.entries(data)) {
    addCategory(category, items);
  }
});

// ---- FOR VISUALS ONLY (AI Assisted) ----
function colorResistor(imgElement, value) {
  // Resistor color code mapping
  const colorCodes = {
    0: '#000000', // Black
    1: '#996633', // Brown
    2: '#FF0000', // Red
    3: '#FF9900', // Orange
    4: '#FFFF00', // Yellow
    5: '#00FF00', // Green
    6: '#0000FF', // Blue
    7: '#FF00FF', // Violet
    8: '#CCCCCC', // Gray
    9: '#FFFFFF'  // White
  };
  
  const multiplierColors = {
    1: '#000000',      // Black (x1)
    10: '#996633',     // Brown (x10)
    100: '#FF0000',    // Red (x100)
    1000: '#FF9900',   // Orange (x1k)
    10000: '#FFFF00',  // Yellow (x10k)
    100000: '#00FF00', // Green (x100k)
    1000000: '#0000FF' // Blue (x1M)
  };
  
  // Parse the resistance value
  function parseResistance(val) {
    val = val.toLowerCase().trim();
    let numericValue;
    
    if (val.includes('k')) {
      numericValue = parseFloat(val.replace('k', '')) * 1000;
    } else if (val.includes('m')) {
      numericValue = parseFloat(val.replace('m', '')) * 1000000;
    } else {
      numericValue = parseFloat(val);
    }
    
    return numericValue;
  }
  
  // Get significant digits and multiplier
  function getColorBands(resistance) {
    let resistanceStr = resistance.toString();
    
    // Get first two significant digits
    let digit1 = parseInt(resistanceStr[0]);
    let digit2 = resistanceStr.length > 1 ? parseInt(resistanceStr[1]) : 0;
    
    // Calculate multiplier (number of zeros after first two digits)
    let multiplier = Math.pow(10, resistanceStr.length - 2);
    
    // Handle special cases like 3.3k -> 3300
    if (resistanceStr.includes('.')) {
      const parts = resistance.toExponential().split('e');
      const significand = parseFloat(parts[0]);
      digit1 = parseInt(significand.toString()[0]);
      digit2 = parseInt(significand.toString()[2] || '0');
      multiplier = Math.pow(10, parseInt(parts[1]) - 1);
    }
    
    return {
      band1: colorCodes[digit1],
      band2: colorCodes[digit2],
      band3: multiplierColors[multiplier] || colorCodes[0]
    };
  }
  
  const resistance = parseResistance(value);
  const colors = getColorBands(resistance);
  
  // Fetch and modify the SVG
  fetch('/images/Resistor.svg')
    .then(response => response.text())
    .then(svgText => {
      // Parse SVG
      const parser = new DOMParser();
      const svgDoc = parser.parseFromString(svgText, 'image/svg+xml');
      const svg = svgDoc.documentElement;

      // Find the color bands by ID and update their fill colors
      const band1 = svg.querySelector('#band-1');
      const band2 = svg.querySelector('#band-2');
      const band3 = svg.querySelector('#band-3');
      
      if (band1) band1.setAttribute('fill', colors.band1);
      if (band2) band2.setAttribute('fill', colors.band2);
      if (band3) band3.setAttribute('fill', colors.band3);

      // Convert modified SVG to data URL
      const serializer = new XMLSerializer();
      const modifiedSvg = serializer.serializeToString(svg);
      const dataUrl = 'data:image/svg+xml;base64,' + btoa(modifiedSvg);
      
      // Update the img element's src
      imgElement.src = dataUrl;
    })
    .catch(error => {
      console.error('Error loading resistor SVG:', error);
      // Keep the original image on error
    });
}
