{
  description = "Dev environment for Python on Raspberry Pi";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };

        runScript = pkgs.writeShellScriptBin "run" ''
          uvicorn main:app --host 0.0.0.0 --port 8080
        '';
      in {
        devShells.default = pkgs.mkShell {
          packages = with pkgs; [
            (python313.withPackages (p: with p; [
              requests
              python-dotenv
              pandas
              fastapi
              uvicorn
              websockets
            ]))
            runScript
          ];
        };
      });
}
