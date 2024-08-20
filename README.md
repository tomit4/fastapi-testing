# FastAPI Testing

This simple project documents how to run simple tests with FastAPI. It is simply
a following along of the
[FastAPI Tutorial On The Subject](https://fastapi.tiangolo.com/tutorial/testing/).

**Getting Started:**

To use this as a basic template for future projects, you'll first need to have
[git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git),
[python](https://www.python.org/downloads/),
[pip](https://pip.pypa.io/en/stable/installation/), and
[rye](https://rye.astral.sh/guide/installation/) installed.

You'll also probably want to have a basic familiarity with the command line
(examples here are in
[bash](https://www.gnu.org/software/bash/manual/bash.html)).

Once those are installed, you can clone this repository in a directory of your
choosing:

```sh
git clone https://github.com/tomit4/fastapi-testing &&\
cd fastapi-testing
```

You'll also need to simply copy the included `env-sample` file as a `.env` to
adjust from the default `HOST` and `PORT`:

```sh
cp env-sample .env
```

Once cloned and inside the project's directory. go ahead and use rye to initiate
the virtual environment (defaults to a `.venv` directory):

```sh
rye sync
```

This will also install all necessary dependencies needed. After that, you'll
need to instantiate your virtual environment like so:

```sh
source .venv/bin/activate
```

After that, you can run the server itself using the `dev` script:

```sh
rye run dev
```

The port utilized for this project is 5173. So once you see the fastapi-cli's
output, indicating successful startup of the server, you can simply navigate in
your browser to localhost:5173/docs to see the OpenAPI documentation of the app.

If you wish to run the tests, simply invoke `rye test` to run them (uses
`pytest` under the hood, do <em>not</em> invoke `pytest` directly as that will
error out when trying to import dependencies):

```sh
rye test
```
