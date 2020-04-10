PS C:\Users\am_cl\OneDrive\Documents\repos\Sprints\Sprint-Challenge--Hash-BC\blockchain> python miner.py
ID is AMC

Searching for next proof
Proof found: 13001553 in 1.2495168999999997
Proof valid but already submitted.
Searching for next proof
Proof found: 16819273 in 1.6103248000000008
Proof valid but already submitted.
Searching for next proof
Proof found: 59912400 in 4.700017199999998
Proof valid but already submitted.
Searching for next proof
Proof found: 50840389 in 4.310146899999992
Proof valid but already submitted.
Searching for next proof
Proof found: 28836947 in 2.974886799999993
Proof valid but already submitted.
Traceback (most recent call last):
  File "miner.py", line 72, in <module>
    r = requests.get(url=node + "/last_proof")
  File "C:\Users\am_cl\.virtualenvs\Sprint-Challenge--Hash-BC-puEHw8vR\lib\site-packages\requests\api.py", line 76, in get
    return request('get', url, params=params, **kwargs)
  File "C:\Users\am_cl\.virtualenvs\Sprint-Challenge--Hash-BC-puEHw8vR\lib\site-packages\requests\api.py", line 61, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\am_cl\.virtualenvs\Sprint-Challenge--Hash-BC-puEHw8vR\lib\site-packages\requests\sessions.py", line 530, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\am_cl\.virtualenvs\Sprint-Challenge--Hash-BC-puEHw8vR\lib\site-packages\requests\sessions.py", line 643, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\am_cl\.virtualenvs\Sprint-Challenge--Hash-BC-puEHw8vR\lib\site-packages\requests\adapters.py", line 439, in send
    resp = conn.urlopen(
  File "C:\Users\am_cl\.virtualenvs\Sprint-Challenge--Hash-BC-puEHw8vR\lib\site-packages\urllib3\connectionpool.py", line 665, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\am_cl\.virtualenvs\Sprint-Challenge--Hash-BC-puEHw8vR\lib\site-packages\urllib3\connectionpool.py", line 421, in _make_request 
    six.raise_from(e, None)
  File "<string>", line 3, in raise_from
  File "C:\Users\am_cl\.virtualenvs\Sprint-Challenge--Hash-BC-puEHw8vR\lib\site-packages\urllib3\connectionpool.py", line 416, in _make_request 
    httplib_response = conn.getresponse()
  File "C:\Users\am_cl\AppData\Local\Programs\Python\Python38-32\lib\http\client.py", line 1322, in getresponse
  File "C:\Users\am_cl\AppData\Local\Programs\Python\Python38-32\lib\http\client.py", line 303, in begin
    version, status, reason = self._read_status()
  File "C:\Users\am_cl\AppData\Local\Programs\Python\Python38-32\lib\http\client.py", line 264, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
  File "C:\Users\am_cl\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 669, in readinto
    return self._sock.recv_into(b)
  File "C:\Users\am_cl\AppData\Local\Programs\Python\Python38-32\lib\ssl.py", line 1241, in recv_into
    return self.read(nbytes, buffer)
  File "C:\Users\am_cl\AppData\Local\Programs\Python\Python38-32\lib\ssl.py", line 1099, in read
    return self._sslobj.read(len, buffer)
KeyboardInterrupt
PS C:\Users\am_cl\OneDrive\Documents\repos\Sprints\Sprint-Challenge--Hash-BC\blockchain> python miner.py
ID is AMC

Searching for next proof
Proof found: 26940572 in 2.437605999999999
Proof valid but already submitted.
Searching for next proof
Proof found: 38268913 in 3.419711899999996
Invalid Proof or valid for block older than last 100 blocks.
Searching for next proof
Proof found: 14123813 in 1.3460575000000006
Total coins mined: 1
Searching for next proof
Proof found: 76404359 in 6.197440999999998
Proof valid but already submitted.
Searching for next proof
Proof found: 1552410 in 0.14980679999999325
Proof valid but already submitted.
Searching for next proof
Proof found: 367996 in 0.036613400000007346
Invalid Proof or valid for block older than last 100 blocks.
Searching for next proof
Proof found: 181406070 in 13.909031400000003
Invalid Proof or valid for block older than last 100 blocks.
Proof valid but already submitted.
Searching for next proof
Traceback (most recent call last):
  File "miner.py", line 74, in <module>
    new_proof = proof_of_work(data.get('proof'))
  File "miner.py", line 31, in proof_of_work
    proof += random.randint(1, 100)
  File "C:\Users\am_cl\AppData\Local\Programs\Python\Python38-32\lib\random.py", line 248, in randint
    return self.randrange(a, b+1)
KeyboardInterrupt
PS C:\Users\am_cl\OneDrive\Documents\repos\Sprints\Sprint-Challenge--Hash-BC\blockchain> python miner.py https://lambda-coin-test-1.herokuapp.com/api
ID is AMC

Searching for next proof
Proof found: 27223552 in 3.0873691
Total coins mined: 1
Searching for next proof
Proof found: 15781659 in 1.3951497999999996
Total coins mined: 2
Searching for next proof
Proof found: 114450947 in 9.286623800000001
Total coins mined: 3
Searching for next proof
Proof found: 13323384 in 0.9916654999999999
Total coins mined: 4
Searching for next proof
Proof found: 46739851 in 4.4871318
Total coins mined: 5
Searching for next proof
Proof found: 37427459 in 3.5519281000000014
Total coins mined: 6
Searching for next proof
Proof found: 72836813 in 5.895995999999997
Total coins mined: 7
Searching for next proof
Proof found: 1903699 in 0.1493602999999979
Total coins mined: 8
Searching for next proof
Proof found: 86309328 in 10.920425200000004
Total coins mined: 9
Searching for next proof
Proof found: 37626287 in 3.157174699999999
Total coins mined: 10
Searching for next proof
Proof found: 80275720 in 8.508571400000001
Total coins mined: 11
Searching for next proof
Proof found: 17780711 in 1.8356645000000071
Total coins mined: 12
Searching for next proof
Proof found: 4536465 in 0.335396099999997
Total coins mined: 13
Searching for next proof
Proof found: 36659435 in 3.0173512000000073
Total coins mined: 14
Searching for next proof
Proof found: 89421058 in 9.089382200000003
Total coins mined: 15
Searching for next proof
Proof found: 62199809 in 7.9037668
Total coins mined: 16
Searching for next proof
Proof found: 1505055 in 0.20725170000000048
Total coins mined: 17
Searching for next proof
Proof found: 73229713 in 9.722777899999997
Total coins mined: 18
Searching for next proof
Proof found: 101033148 in 10.300269600000007
Total coins mined: 19
Searching for next proof
Proof found: 1909469 in 0.3241279000000077
Total coins mined: 20
Searching for next proof
Proof found: 112985656 in 15.595546499999998
Proof valid but already submitted.
Searching for next proof
Proof found: 69000818 in 6.186101899999983
Total coins mined: 21
Searching for next proof
Proof found: 112472008 in 9.094943799999982
Total coins mined: 22
Searching for next proof
Proof found: 26370187 in 2.077077700000018
Total coins mined: 23
Searching for next proof
Proof found: 12823643 in 0.9522938000000067
Total coins mined: 24
Searching for next proof
Proof found: 16556217 in 1.1271292999999787
Total coins mined: 25
Searching for next proof
Proof found: 4165953 in 0.28623049999998784
Total coins mined: 26
Searching for next proof
Proof found: 1940591 in 0.1486773000000028
Total coins mined: 27
Searching for next proof
Proof found: 17326488 in 1.447561300000018
Total coins mined: 28
Searching for next proof
Proof found: 25027420 in 1.6953027000000134
Total coins mined: 29
Searching for next proof
Proof found: 19917300 in 1.3761495999999909
Total coins mined: 30
Searching for next proof
Proof found: 79999628 in 5.386048499999987
Proof valid but already submitted.
Searching for next proof
Proof found: 5610551 in 0.3948852000000045
Total coins mined: 31
Searching for next proof
Proof found: 51275472 in 3.4317522000000054
Proof valid but already submitted.
Searching for next proof
Proof found: 55102660 in 3.7846126999999967
Proof valid but already submitted.
Searching for next proof
Proof found: 31612439 in 2.1020895999999993
Total coins mined: 32
Searching for next proof
Proof found: 38806815 in 2.6488099999999974
Total coins mined: 33
Searching for next proof
Proof found: 40010344 in 2.7371872000000224
Total coins mined: 34
Searching for next proof
Proof found: 35560192 in 2.408429099999978
Total coins mined: 35
Searching for next proof
Proof found: 36984180 in 2.464527799999985
Total coins mined: 36
Searching for next proof
Traceback (most recent call last):
  File "miner.py", line 74, in <module>
    new_proof = proof_of_work(data.get('proof'))
  File "miner.py", line 30, in proof_of_work
    while valid_proof(last_hash, proof) is False:
  File "miner.py", line 47, in valid_proof
    guess = hashlib.sha256(str(proof).encode()).hexdigest()
KeyboardInterrupt
PS C:\Users\am_cl\OneDrive\Documents\repos\Sprints\Sprint-Challenge--Hash-BC\blockchain>