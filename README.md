# Musterlösung für HSM part
Dies ist sind die Übungen für den HSM teil des Kurses "Crypto Security Professional" von is-its.
Die eigentlichen Daten sind in Branches, also bitte dorthin wechseln:
```bash
git branch
git checkout uebung1
```

# Installation
Getestet auf Ubuntu 22.04 mit AWS AMI ami-0a24ce26f4e187f9a
```bash
sudo apt update -y
sudo apt install -y python3 python3-pip python3-flask git libssl-dev libgmp3-dev
sudo -H pip3 install Flask-JSON python-bitcoinlib 
git clone https://github.com/icehawk1/hsm_lecture.git
```

