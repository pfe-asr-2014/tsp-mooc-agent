# tsp-mooc-agent
Container collecting logs from running containers on the learner's computer

## Configure

Configure your Moodle credentials in `app/login.yml` :
```yaml
username: "my username"
password: my password"
```

Then configure the application in `app/agent.yml` :
```yaml
# your MQTT broker container
server: "tsp-mooc-broker"
# the string to filter logs
filter: "POST"
# the MQTT topic used to report the events
topic: "mooc/"
```

## License

This software is distributed under the terms of the MIT license. See [LICENSE](./LICENSE) for details.
