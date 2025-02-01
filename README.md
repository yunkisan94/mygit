README

프로젝트 설명
이 프로젝트는 ccxt 라이브러리를 활용하여 Binance 거래소의 시장 데이터를 가져오고, USDT 페어로 거래되는 모든 마켓을 출력하는 간단한 스크립트입니다.

설치 방법

1. Python이 시스템에 설치되어 있는지 확인하세요.

2. 다음 명령어를 사용하여 ccxt 라이브러리를 설치하세요:
   pip install ccxt

사용 방법

1. 스크립트를 실행하면 Binance의 모든 마켓 중 USDT 페어로 거래되는 마켓 목록을 확인할 수 있습니다.
2. 코드 내 주석 처리된 부분을 활성화하면 추가적인 정보를 출력할 수 있습니다.

import ccxt

binance = ccxt.binance()
markets = binance.load_markets()

for market in markets.keys():
    if market.endswith("USDT"):
        print(market)

README

Project Description
This project features a simple script that utilizes the ccxt library to fetch market data from the Binance exchange and display all markets traded against USDT.

Installation

1. Ensure that Python is installed on your system.

2. Install the ccxt library using the following command:
   pip install ccxt

Usage

1. Run the script to view a list of all USDT-paired markets available on Binance.
2. Uncomment the relevant sections in the code to display additional information if needed.

import ccxt

binance = ccxt.binance()
markets = binance.load_markets()

for market in markets.keys():
    if market.endswith("USDT"):
        print(market)
