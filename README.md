## Getting started
1. Clone this Repository:
```
git clone git@github.com:tpatop/crypto_telethon.git
cd crypto_telethon
```
2. Install Dependencies:
   * Install Docker and Docker-compose
3. Configure Environment Variables:
   * Create a `.env` file and populate it using the provided `.env.example` as a template. You can use the variables from the example without changes or create a copy and rename it to `.env`.
```
cp .env.example .env
```

## Usage

### Running development version:
```
make start
```
If you are launching the application for the first time, you will need to enter the number and confirmation code in the telegram application in the terminal.

### Stop the applications
```
make stop
```
### Delete the applications
```
make delete
```
This action does not delete the repository and created files while the application is running.

## Documentation
* API crypto - http://localhost:8080/docs
* flower - http://localhost:5557

## Additional Information
* API_KEY - https://status.coinlayer.com/
* API_TG_ID, API_TG_HASH - https://my.telegram.org/


## Contributing

You can contribute by opening issues or creating pull requests.
