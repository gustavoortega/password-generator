# Password Generator



<h1>Instructions for containerized usage</h1>

```
git clone https://github.com/gustavoortega/password-generator.git

cd password-generator/

docker build -t local:password .

docker run --rm -it -p 5000:5000 local:password
```

Now, it's time to use it!
```
curl 'http://localhost:5000/generate-password?lowercase=10&uppercase=10&digits=10&length=50' 

{"password": "VoxDuyPHJjo0yw4sWBe4gdbSVAz9k4cv5toA3HOM5w6XRieuY7"}

```


<h1>Instructions for usage on local machine</h1>

```

git clone https://github.com/gustavoortega/password-generator.git

cd password-generator/

pip3 install -r ./requirements.txt

python3 ./main.py
```
