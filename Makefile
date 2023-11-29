DC = docker-compose
DEV_COMPOSE = -f dev.docker-compose.yml

.PHONY: astart stop delete

start: ## up development version
	$(DC) $(DEV_COMPOSE) up -d
	docker exec -it webpegas_celery_worker_1 python api_telegram/registration.py

stop: ## stop development vesrion
	$(DC) $(DEV_COMPOSE) down

delete: ## delete all containers/images
	docker system prune -a --volumes
