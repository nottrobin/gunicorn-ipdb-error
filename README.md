# Talisker breaks ipdb for gunicorn gevent

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
./run-with-gunicorn
```

Now if you run `curl localhost:8000`, it should jump into an `ipdb` shell.

Now if you `pip3 install talisker`, and then run `run-with-gunicorn` again, now when you do `curl localhost:8000` you should see:

```
...
  File "/home/robin/Projects/gunicorn-ipdb-error/.venv/lib/python3.6/site-packages/prompt_toolkit/application/current.py", line 70, in <module>
    "_current_app_session", default=AppSession()
TypeError: 'type' object is not subscriptable
```
