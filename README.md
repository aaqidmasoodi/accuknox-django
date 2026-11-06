# AccuKnox Django Trainee Assignment

## Setup

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements-dev.txt
python manage.py migrate
```

## Django Signals

The examples use a `post_save` receiver on `Order` (`signals_demo/signals.py`).

### Q1. Are signals synchronous or asynchronous by default?

Synchronous. `save()` doesn't return until every receiver has run. The receiver sleeps for 2 seconds and `save()` takes 2 seconds to return.

```bash
python manage.py q1_sync
```
```
Receiver sleeps for 2s
save() returned after 2.02s
Receiver finished before save() returned: True
Synchronous: the caller waited for the receiver.
```
