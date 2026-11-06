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

### Q2. Do signals run in the same thread as the caller?

Yes. The caller and the receiver report the same thread id.

```bash
python manage.py q2_thread
```
```
Caller thread:   140228205266752
Receiver thread: 140228205266752
Same thread.
```

### Q3. Do signals run in the same database transaction as the caller?

Yes. Inside `transaction.atomic()` the order is saved and the receiver writes a `SignalLog` row. When the transaction is rolled back, the `SignalLog` row is gone as well, so the receiver's write was part of the same transaction.

```bash
python manage.py q3_transaction
```
```
SignalLog rows inside the transaction: 1
Receiver in atomic block: True
After rollback: 0 orders, 0 signal logs
Same transaction: the receiver's write was rolled back too.
```
