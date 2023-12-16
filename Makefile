DC = docker-compose
DEV_COMPOSE = -f dev.docker-compose.yml

.PHONY: start stop delete

start: ## up development version
	$(DC) $(DEV_COMPOSE) up -d
	docker exec -it webpegas_celery_worker_1 python main.py

start-build: ## up development version with build
	$(DC) $(DEV_COMPOSE) up --build -d
	docker exec -it webpegas_celery_worker_1 python main.py

stop: ## stop development vesrion
	$(DC) $(DEV_COMPOSE) down

delete: ## delete all containers/images
	docker system prune -a --volumes
