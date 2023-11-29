DC = docker-compose
DEV_COMPOSE = -f dev.docker-compose.yml

.PHONY: astart stop delete registration

start: ## up development version
	$(DC) $(DEV_COMPOSE) up

stop: ## stop development vesrion
	$(DC) $(DEV_COMPOSE) down

delete: ## delete all containers/images
	docker system prune -a --volumes

registration: ## Create session file and first start script
	docker exec -it webpegas_celery_worker_1 python api_telegram/registration.py