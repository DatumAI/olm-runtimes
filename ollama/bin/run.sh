# run container publishing port 80 to 8080
docker run -it -p 8080:80 -p 8081:11434 --rm blewandowskidatumai/olm-ollama-runtime:latest
