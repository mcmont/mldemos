run-iphone:
	TRAINING_DATA="training_data/iphone.csv" python3 demo.py --port 8000

train:
	python3 demo.py --port 8000 --train

certs:
	openssl req -x509 -newkey rsa:2048 -nodes -out cert.pem -keyout key.pem -days 365
