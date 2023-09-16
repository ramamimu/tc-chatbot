# Rasa Chatbot Documentation

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

### Code Flow

add your classes on `actions/actions.py`, then create custom action class. Each class name must start with `Action*`.

> Don't forget to add your action item name to `domain.yml`
