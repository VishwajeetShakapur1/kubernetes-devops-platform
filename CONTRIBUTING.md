# Contributing

This is primarily a personal learning and portfolio repository.

Before opening a change:

```bash
python -m compileall app
python -m unittest discover -s app/tests -v
```

Keep Kubernetes resources small and explicit. Avoid committing credentials, kubeconfigs or environment-specific secrets.
