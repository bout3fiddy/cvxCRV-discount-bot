# Convex Finance Discord Chat Bot


Watches the SushiSwap pool ratio between cvxCRV and CRV tokens and reports it on the Convex Finance Discord sidebar:

<img width="249" alt="Screenshot 2021-07-16 at 00 49 54" src="https://user-images.githubusercontent.com/11488427/125867657-9df3c625-ae5c-4360-987e-d1291d4a6200.png">

cvxCRV token: https://etherscan.io/token/0x62b9c7356a2dc64a1969e19c23e4f579f9810aa7
CRV token: https://etherscan.io/token/0xD533a949740bb3306d119CC777fa900bA034cd52
SushiSwap Router Contract: https://etherscan.io/address/0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f


The assets are not pegged to each other. cvxCRV is minted by locking CRV into veCRV by the Convex Finance platform. This lock is perpetual. The SushiSwap liquidity pool offers exit liquidity to liquidity providers, thus making veCRV liquid.

The value of cvxCRV with respect to CRV swings with the market, but has the potential to return to 1:1 (this is something that the market decides).

This repo calls the SushiSwap Router contract to calculate the amount of cvxCRV obtained by swapping 1000 CRV tokens.

<img width="693" alt="Screenshot 2021-07-15 at 02 07 30" src="https://user-images.githubusercontent.com/11488427/125867985-a42f544d-4b6e-4165-8d61-836f65053c46.png">

The app is deployed on Heroku, requires an APi key to access Ethereum node data. The deployment uses Infura (https://infura.io/)
