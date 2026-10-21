# Mercado Vecino - Despliegue con Docker Compose

Plataforma contenerizada de 3 capas + caché Redis.

## Requisitos
- Docker Engine 24+ con Docker Compose v2.

## Pasos para desplegar
1. Entrar a la carpeta: `cd mercado-vecino`
2. Crear archivo de entorno: `cp .env.example .env`
3. Levantar todo el stack: `docker compose up -d --build`
4. Verificar el estado: `docker compose ps`
