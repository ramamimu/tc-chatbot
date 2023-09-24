# Rasa Chatbot Documentation

## How to run

> Using Docker

Make sure you have changed in file `endpoints.yml` row 14 from `url: "http://localhost:5055/webhook"` to be `url: "http://actions:5055/webhook`

### Docker Compose Build

```bash
docker compose build
```

### Docker Compose Run


```bash
docker compose up
```

> without showing terminal logs

```bash
docker compose up -d
```

__wait for 5 - 10 seconds to make sure the program already running properly__

## How to stop

```bash
docker compose down
```

## Rest API

host: `localhost:5002`

### request

```bash
POST /webhooks/rest/webhook
{
    message: string
}
```

### response
```bash
[
    {
        "recipient_id": "default",
        "text": string
    }
]
```


## Custom Actions

### Configuration

setting up in `endpoints.yml` then uncoment this row

```yml
action_endpoint:
 url: "http://localhost:5055/webhook"
```

for running, need two terminal which are run

```sh
rasa shell
```

```sh
rasa run actions
```

> if you are running on the docker, please __change manually the host__ in `endpoints.yml`

### Code Flow

add your classes on `actions/actions.py`, then create custom action class. Each class name must start with `Action*`

> Don't forget to add your action item name to `domain.yml`
