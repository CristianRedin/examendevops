build:
	docker build -t ghcr.io/cristianredin/examendevops:1.0.5 .

deploy:
	docker stack deploy --with-registry-auth -c stack.yml redin
rm:
	docker stack rm redin