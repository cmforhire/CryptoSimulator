'''
author: Calen Mitchell
This is a cryptocurrency simulator Test File
Used for adding ideas to the game to make it more entertaining
Can You make it past 1 Millon? Try and see! 
'''

import os, sys, random, copy



myCash = random.uniform(2000.0, 15500.0)
myCash = round(myCash, 2)
# your wallet of total dollars you have
yourWallet = float(myCash)
#copy.copy method from copy import module
beginBalance = copy.copy(yourWallet)

endBalance = 0.0    # used to find difference of lifetime earnings

steveResponsible = 0.0  # used to keep track of Steve's shenanigans

carInsurance = 500.0  # Car insurance bill

# Your CryptoCurrency Wallet
myBtc, myEth, myXrp, myXlm, myTrx = 0.0, 0.0, 0.0, 0.0, 0.0
myCryptoWallet = ['My Bitcoin: '+str(myBtc) + ', ', 'My Ethereum: '+str(myEth) + ', ',
                  'My Ripple: '+str(myXrp) + ', ', 'My Stellar: '+str(myXlm) + ', ','My Tron: '+str(myTrx)]

# list of cryptocurrencies
listing = ['Bitcoin', 'Ethereum', 'Ripple', 'Stellar', 'Tron']

# acronym representations
btc, eth, xrp, xlm, trx = listing

# pricing for each coin
btcPrice, ethPrice, xrpPrice, xlmPrice, trxPrice = 1000, 300, .50, .30, .05
prices = ['bitcoin: $'+str(btcPrice), 'ethereum: $'+str(ethPrice), 'ripple: $'+str(xrpPrice), 'stellar: $'+str(xlmPrice), 'Tron: $'+str(trxPrice)]


# code for getting profile
def getProfile():
    profile = [myName, '$'+str(myCash), myCryptoWallet]
    print(str(profile))
    print('')
    print('')

# further information on different cryptos available
def cryptoInfo():
    print('Bitcoin: the leader of them all. First ever cryptocurrency.')
    print('Ethereum: Similar to bitcoin, but known for smart contracts')
    print('Ripple: Real-time cross border transactions in 3 seconds flat')
    print('Stellar: Connects banks, payment systems, and people and performs at almost no cost')
    print('Tron: aims to create a global free content entertainment system')
    print('')

def takeStock(debt):
    global myBtc, myEth, myXrp, myXlm, myTrx, myCash, myCryptoWallet
    soldBtc, soldEth, soldXrp, soldXlm, soldTrx = 0, 0, 0, 0, 0
    if myBtc == 0 and myEth == 0 and myXrp == 0 and myXlm == 0 and myTrx ==0:
        print('The game had to end because your debt could not be paid. ')
        print('You are now bankrupt.')
        print('Thank you for playing!')
        exit()

    while True:
        choice = random.randint(0, 5)
        if float(debt) > myCash:
            if choice == 0:
                if myBtc >= 1:
                    myBtc = myBtc - 1
                    myCryptoWallet[0] = 'My Bitcoin: ' + str(myBtc) + ', '
                    myCash = round(myCash + btcPrice, 2)
                    soldBtc += 1
                else:
                    continue


            elif choice == 1:
                if myEth >= 1:
                    myEth = myEth - 1
                    myCryptoWallet[1] = 'My Ethereum: ' + str(myEth) + ', '
                    myCash = round(myCash + ethPrice, 2)
                    soldEth += 1
                else:
                    continue


            elif choice == 2:
                if myXrp >= 1:
                    myXrp = myXrp - 1
                    myCryptoWallet[2] = 'My Ripple: ' + str(myXrp) + ', '
                    myCash = round(myCash + xrpPrice, 2)
                    soldXrp += 1

                else:
                    continue

            elif choice == 3:
                if myXlm >= 1:
                    myXlm = myXlm - 1
                    myCryptoWallet[3] = 'My Stellar: ' + str(myXlm) + ', '
                    myCash = round(myCash + xlmPrice, 2)
                    soldXlm += 1
                else:
                    continue

            elif choice == 4:
                if myTrx >= 1:
                    myTrx = myTrx - 1
                    myCryptoWallet[4] = 'My Tron: ' + str(myTrx) + ', '
                    myCash = round(myCash + trxPrice, 2)
                    soldTrx += 1

                else:
                    continue
        else:
            break

    if soldBtc > 0 or soldEth > 0 or soldXrp > 0 or soldXlm > 0 or soldTrx > 0:
        print('We had to confiscate: ' + str(int(soldBtc)) + ' Bitcoins, ' + str(int(soldEth)) + ' Ethereum, '
              + str(int(soldXrp)) + ' Ripple(s), ' + str(int(soldXlm)) + ' Stellar token(s), and ' + str(
            int(soldTrx)) + ' Tron token(s)')
        print(' Your debt of ' + str(debt) + ' was paid in full. Thank you.')
        print('')
        soldBtc, soldEth, soldXrp, soldXlm, soldTrx = 0, 0, 0, 0, 0
    else:
        print('We did not have to confiscate any investments at this time.')
        print(' Your debt of ' + str(debt) + ' was paid in full. Thank you.')


# method to ensure the bill is able to be paid in the debt function
def isDebt(debt):
    print('')
    global myBtc, myEth, myXrp, myXlm, myTrx, myCash, myCryptoWallet
    if debt > myCash:
        takeStock(debt)

def checkIfThere():
    if myBtc == 0 and myEth == 0 and myXrp == 0 and myXlm == 0 and myTrx ==0:
        print('The game had to end because your debt could not be paid. ')
        print('You are now bankrupt.')
        print('Thank you for playing!')
        exit()

# random bills that pop up in the mix
def debt():
    print('')
    global myBtc, myEth, myXrp, myXlm, myTrx, myCash, myCryptoWallet, carInsurance
    soldBtc, soldEth, soldXrp, soldXlm, soldTrx = 0, 0, 0, 0, 0
    global myCash, steveResponsible
    checkIfThere()

    if myCash < 100000:
        mortgage = 1200.0
    else:
        mortgage = round(float(myCash * .07), 2)

    debtChoice = random.randint(0, 12)

    if debtChoice == 1:
        max = random.randint(3, 7)
        i = 0
        while i < max:
            choice = random.randint(0, 5)

            if choice == 0:
                if myBtc >= 1:
                    myBtc = myBtc - 1
                    myCryptoWallet[0] = 'My Bitcoin: ' + str(myBtc) + ', '
                    myCash = round(myCash + btcPrice, 2)
                    soldBtc += 1
                    continue

            elif choice == 1:
                if myEth >= 1:
                    myEth = myEth - 1
                    myCryptoWallet[1] = 'My Ethereum: ' + str(myEth) + ', '
                    myCash = round(myCash + ethPrice, 2)
                    soldEth += 1
                    continue


            elif choice == 2:
                if myXrp >= 1:
                    myXrp = myXrp - 1
                    myCryptoWallet[2] = 'My Ripple: ' + str(myXrp) + ', '
                    myCash = round(myCash + xrpPrice, 2)
                    soldXrp += 1
                    continue



            elif choice == 3:
                if myXlm >= 1:
                    myXlm = myXlm - 1
                    myCryptoWallet[3] = 'My Stellar: ' + str(myXlm) + ', '
                    myCash = round(myCash + xlmPrice, 2)
                    soldXlm += 1
                    continue


            elif choice == 4:
                if myTrx >= 1:
                    myTrx = myTrx - 1
                    myCryptoWallet[4] = 'My Tron: ' + str(myTrx) + ', '
                    myCash = round(myCash + trxPrice, 2)
                    soldTrx += 1
                    continue
            else:
                break



        print('The IRS took 40% of your total earnings, along with '+ str(int(soldBtc)) + ' Bitcoins, ' + str(int(soldEth)) + ' Ethereum, '
              + str(int(soldXrp)) + ' Ripple(s), ' + str(int(soldXlm)) + ' Stellar token(s), and ' + str(
            int(soldTrx)) + ' Tron token(s)')

        print('Previous: '+str(myCash))
        myCash = round(float(myCash - (myCash * .40)), 2)
        print('New Balance: '+str(myCash))
        print('')


    elif debtChoice == 3:
        print('You have to pay your car insurance Total: '+str(carInsurance))
        checkIfThere()
        if carInsurance > myCash:
            isDebt(carInsurance)
            print('Previous: ' + str(myCash))
            myCash = float(myCash - carInsurance)
            myCash = round(myCash, 2)
            print('New Balance: ' + str(myCash))
            print('')
        else:
            print('Previous: ' + str(myCash))
            myCash = float(myCash - carInsurance)
            myCash = round(myCash, 2)
            print('New Balance: ' + str(myCash))
            print('')

    elif debtChoice == 5:
        print('You have to pay Mortgage: ' + str(mortgage))
        checkIfThere()
        if mortgage > myCash:
            isDebt(mortgage)
            print('Previous: ' + str(myCash))
            myCash = round(float(myCash - mortgage), 2)
            print('New Balance: ' + str(myCash))
            print('')
        else:
            print('Previous: ' + str(myCash))
            myCash = round(float(myCash - mortgage), 2)
            print('New Balance: ' + str(myCash))
            print('')


    elif debtChoice == 9:
        print('Your son Steve crashed your car. Your insurance is now higher.')
        print('Previous Insurance Rate: '+str(carInsurance))
        carInsurance = round(carInsurance +250.0, 2)
        print('New Insurance Rate: '+str(carInsurance))
        checkIfThere()
        if carInsurance > myCash:
            isDebt(carInsurance)
            print('Previous Balance: ' + str(myCash))
            myCash = round(float(myCash - carInsurance), 2)
            print('New Balance: ' + str(myCash))
            steveResponsible = round(float(steveResponsible + 250.0), 2)
            print('')
        else:
            print('Previous Balance: ' + str(myCash))
            myCash = round(float(myCash - carInsurance), 2)
            print('New Balance: ' + str(myCash))
            steveResponsible = round(float(steveResponsible + 250.0), 2)
            print('')

    elif debtChoice == 0:
        print('Your son Steve donated some of your money because he was happy.')
        donation = round(float(myCash * .10), 2)
        print('Steve donated: $'+str(donation))
        print('Previous Balance: '+str(myCash))
        myCash = round(float(myCash - donation), 2)
        print('New Balance: '+str(myCash)+', Steve is happy.')
        steveResponsible = round(float(steveResponsible + donation), 2)
        print('')


    else:
        print('Debt: You do not owe anything at this time.')
        print('')
# end of debt method

#method used to ensure stock prices do not remain at 0.0
def ifZero():
    global btcPrice, ethPrice, xrpPrice, xlmPrice, trxPrice
    if btcPrice == 0.0:
        btcPrice = random.uniform(50, 200)
    elif ethPrice == 0.0:
        ethPrice = random.uniform(25, 150)
    elif xrpPrice == 0.0:
        xrpPrice = random.uniform(0, 1.0)
    elif xlmPrice == 0.0:
        xlmPrice = random.uniform(0, 1.0)
    elif trxPrice == 0.0:
        trxPrice = random.uniform(0, .15)
    else:
        print('')

'''
method to randomize the prices
Round limits the float to two decimal places
'''
def randomize():
    global btcPrice, ethPrice, xrpPrice, xlmPrice, trxPrice, prices #global keyword allows me to update global variable
    print('Previous: '+str(prices))
    #if bitcoin goes up, then all go up
    btcChance = random.randint(0, 10)

    if btcChance >= 5:
        rand1 = random.uniform(1.1, 3.5)
    else:
        rand1 = random.uniform(0.3, .8)


    btcPrice = round(btcPrice * rand1, 2)
    if rand1 < 1:
        # if bitcoin falls, chances of profit are rare
        rand2, rand3, rand4, rand5 = random.uniform(0.5, 1.1), random.uniform(0.1, 1.02), random.uniform(0.1, 1.02), random.uniform(0.5, 1.02)

        ethPrice = round(ethPrice * rand2, 2)
        xrpPrice = round(xrpPrice * rand3, 2)
        xlmPrice = round(xlmPrice * rand4, 2)
        trxPrice = round(trxPrice * rand5, 2)
    else:
        # if bitcoin goes up, then profit is more than likely
        rand2, rand3, rand4, rand5 = random.uniform(.95, 3.0), random.uniform(.95, 3.0), random.uniform(.95, 3.0), random.uniform(.95, 3.0)

        ethPrice = round(ethPrice * rand2, 2)
        xrpPrice = round(xrpPrice * rand3, 2)
        xlmPrice = round(xlmPrice * rand4, 2)
        trxPrice = round(trxPrice * rand5, 2)

    #reassigns new prices
    prices = ['bitcoin: $' + str(btcPrice), 'ethereum: $' + str(ethPrice), 'ripple: $' + str(xrpPrice),
              'stellar: $' + str(xlmPrice), 'Tron: $' + str(trxPrice)]

   # print(str(rand1) + ',' + str(rand2) + ',' + str(rand3) + ',' + str(rand4) + ',' + str(rand5))
    print(' -- New Prices -- ')
    print(prices)
    print('')
    print('')
    debt()
    ifZero()

def getCurrentPrices():
    print('Current Prices: '+str(prices))


# method for buying and cryptocurrency
def optionBuy():
    global myBtc, myEth, myXrp, myXlm, myTrx, myCash, myCryptoWallet
    while True:
        print('Which currency would you like to buy? Enter number below')
        print('1 -- Bitcoin, 2 -- Ethereum, 3 -- Ripple, 4 -- Stellar, 5 -- Tron, 6 -- Done Purchasing')
        print(' -- Enter NUMBER ONLY for choice below this Line --')
        response = input()
        try:
            response = int(response)
        except:
            print('Please enter a whole number next time')
            response = 6
        #response for bitcoin
        if response == 1:
            while True:
                getCurrentPrices()
                print('Your Balance: ' + str(myCash))
                print('How many bitcoins would you like to purchase? Integers only')
                desiredAmount = input()
                desiredAmount = float(desiredAmount)
                sumPurchase = btcPrice*desiredAmount
                if sumPurchase > myCash:
                    print('You do not have enough funds to purchase '+str(desiredAmount)+ ' bitcoin(s)')
                    continue
                else:
                    myBtc = myBtc+desiredAmount
                    myCryptoWallet[0] = 'My Bitcoin: '+str(myBtc) + ', '
                    myCash = round(myCash - sumPurchase, 2)
                    print('Remaining Balance: '+str(myCash))
                    break

        # response for Ethereum
        elif response == 2:
            while True:
                getCurrentPrices()
                print('Your Balance: ' + str(myCash))
                print('How many Ethereum tokens would you like to purchase? Integers only')
                desiredAmount = input()
                desiredAmount = float(desiredAmount)
                sumPurchase = ethPrice * desiredAmount
                if sumPurchase > myCash:
                    print('You do not have enough funds to purchase ' + str(desiredAmount) + ' ethereum token(s)')
                    continue
                else:
                    myEth = myEth + desiredAmount
                    myCryptoWallet[1] = 'My Ethereum: ' + str(myEth) + ', '
                    myCash = round(myCash - sumPurchase, 2)
                    print('Remaining Balance: ' + str(myCash))
                    break

        # response for Ripple
        elif response == 3:
            while True:
                getCurrentPrices()
                print('Your Balance: '+str(myCash))
                print('How many Ripple tokens would you like to purchase? Integers only')
                desiredAmount = input()
                desiredAmount = float(desiredAmount)
                sumPurchase = xrpPrice * desiredAmount
                if sumPurchase > myCash:
                    print('You do not have enough funds to purchase ' + str(desiredAmount) + ' XRP token(s)')
                    continue
                else:
                    myXrp = myXrp+desiredAmount
                    myCryptoWallet[2]='My Ripple: ' + str(myXrp) + ', '
                    myCash = round(myCash - sumPurchase, 2)
                    print('Remaining Balance: ' + str(myCash))
                    break

        # response for Stellar
        elif response == 4:
            while True:
                getCurrentPrices()
                print('Your Balance: ' + str(myCash))
                print('How many Stellar tokens would you like to purchase? Integers only')
                desiredAmount = input()
                desiredAmount = float(desiredAmount)

                '''
                insert code for if statement in case the user does not type a number desiredAmount
                '''
                sumPurchase = xlmPrice * desiredAmount
                if sumPurchase > myCash:
                    print('You do not have enough funds to purchase ' + str(desiredAmount) + ' XLM token(s)')
                    continue
                else:
                    myXlm = myXlm+desiredAmount
                    myCryptoWallet[3] = 'My Stellar: '+str(myXlm) + ', '
                    myCash = round(myCash - sumPurchase, 2)
                    print('Remaining Balance: ' + str(myCash))
                    break

        # response for Tron
        elif response == 5:
            while True:
                getCurrentPrices()
                print('Your Balance: ' + str(myCash))
                print('How many Tron tokens would you like to purchase? Integers only')
                desiredAmount = input()
                desiredAmount = float(desiredAmount)
                sumPurchase = trxPrice * desiredAmount
                if sumPurchase > myCash:
                    print('You do not have enough funds to purchase ' + str(desiredAmount) + ' TRX token(s)')
                    continue
                else:
                    myTrx = myTrx+desiredAmount
                    myCryptoWallet[4] = 'My Tron: '+str(myTrx)
                    myCash = round(myCash - sumPurchase, 2)
                    print('Remaining Balance: ' + str(myCash))
                    break

        elif response == 6:
            break

        else:
            print('You did not pick a valid option.')
            continue

        print('Would you like to purchase other tokens? Y or N')
        answer = input()
        answer = answer.lower()
        if answer == 'y' or answer == 'yes':
            continue
        else:
            print('Thank You for your Purchase!')
            break

    getProfile()
    print('')
    print('')

# method to sell cryptocurrency
def optionSell():
    global myBtc, myEth, myXrp, myXlm, myTrx, myCash, myCryptoWallet
    while True:
        print('Which currency would you like to sell? Enter number below')
        print('1 -- Bitcoin, 2 -- Ethereum, 3 -- Ripple, 4 -- Stellar, 5 -- Tron, 6 -- Done Selling')
        print(' -- Enter NUMBER ONLY for choice below this Line --')
        response = input()
        response = int(response)
        # response for bitcoin
        if response == 1:
            while True:
                getCurrentPrices()
                getProfile()
                print('How many bitcoins would you like to sell?')
                sellAmount = input()
                sellAmount = float(sellAmount)
                sumTransaction = btcPrice * sellAmount
                if sellAmount > myBtc:
                    print('You do not have  ' + str(sellAmount) + ' bitcoin(s)')
                    continue
                else:
                    myBtc = myBtc - sellAmount
                    myCryptoWallet[0] = 'My Bitcoin: ' + str(myBtc) + ', '
                    myCash = round(myCash + sumTransaction, 2)
                    print('New Balance: ' + str(myCash))
                    break

        if response == 2:           #ethereum
            while True:
                getCurrentPrices()
                getProfile()
                print('How many ethereum tokens would you like to sell?')
                sellAmount = input()
                sellAmount = float(sellAmount)
                sumTransaction = ethPrice * sellAmount
                if sellAmount > myEth:
                    print('You do not have  ' + str(sellAmount) + ' ethereum token(s)')
                    continue
                else:
                    myEth = myEth - sellAmount
                    myCryptoWallet[1] = 'My Ethereum: ' + str(myEth) + ', '
                    myCash = round(myCash + sumTransaction, 2)
                    print('New Balance: ' + str(myCash))
                    break

        if response == 3:           #ripple
            while True:
                getCurrentPrices()
                getProfile()
                print('How many XRP tokens would you like to sell?')
                sellAmount = input()
                sellAmount = float(sellAmount)
                sumTransaction = xrpPrice * sellAmount
                if sellAmount > myXrp:
                    print('You do not have  ' + str(sellAmount) + ' xrp token(s)')
                    continue
                else:
                    myXrp = myXrp - sellAmount
                    myCryptoWallet[2] = 'My Ripple: ' + str(myXrp) + ', '
                    myCash = round(myCash + sumTransaction, 2)
                    print('New Balance: ' + str(myCash))
                    break

        if response == 4:               #stellar
            while True:
                getCurrentPrices()
                getProfile()
                print('How many stellar tokens would you like to sell?')
                sellAmount = input()
                sellAmount = float(sellAmount)
                sumTransaction = xlmPrice * sellAmount
                if sellAmount > myXlm:
                    print('You do not have  ' + str(sellAmount) + ' xlm token(s)')
                    continue
                else:
                    myXlm = myXlm - sellAmount
                    myCryptoWallet[3] = 'My Stellar: ' + str(myXlm) + ', '
                    myCash = round(myCash + sumTransaction, 2)
                    print('New Balance: ' + str(myCash))
                    break

        if response == 5:       # tron
            while True:
                getCurrentPrices()
                getProfile()
                print('How many tron tokens would you like to sell?')
                sellAmount = input()
                sellAmount = float(sellAmount)
                sumTransaction = trxPrice * sellAmount
                if sellAmount > myTrx:
                    print('You do not have  ' + str(sellAmount) + ' trx token(s)')
                    continue
                else:
                    myTrx = myTrx - sellAmount
                    myCryptoWallet[4] = 'My Tron: ' + str(myTrx) + ', '
                    myCash = round(myCash + sumTransaction, 2)
                    print('New Balance: ' + str(myCash))
                    break

        if response ==6:
            break

        print('Would you like to sell other tokens? Y or N')
        answer = input()
        answer = answer.lower()
        if answer == 'y':
            continue
        else:
            print('New Balance: ' + str(myCash))
            break
    getProfile()
    print('')
    print('')


# method for cashing out/selling all cryptocurrencies FINISH
def cashOut():
    print('')
    global myBtc, myEth, myXrp, myXlm, myTrx, myCash, myCryptoWallet
    sumTransaction =(myBtc * btcPrice) +(myEth * ethPrice) + (myXrp * xrpPrice) + \
                    (myXlm * xlmPrice) + (myTrx * trxPrice)
    myCash = round(myCash + sumTransaction, 2)

    myBtc = myBtc - myBtc
    myEth = myEth - myEth
    myXrp = myXrp - myXrp
    myXlm = myXlm - myXlm
    myTrx = myTrx - myTrx

    print(' -- Game Summary --')
    print('Your beginning balance: ' + str(beginBalance))
    print('Your ending balance: ' + str(myCash))
    totalProfit = float(myCash - beginBalance)
    if totalProfit > 0:
        print('Total profit: ' + str(totalProfit))
        if totalProfit >= 1000000:
            print('You won the Game!')
        else:
            print('You did great, but you did not get over 1 Million in profit!')
    else:
        print('Your total losses: ' + str(totalProfit))
    print('How do you think you did?')
    print('Thank you for playing ' + myName + '!')



# method for selecting the options
def selectOption():
    while True:
        print('What option would you like, '+myName)
        print('1 -- Buy Crypto')
        print('2 -- Sell Crypto')
        print('3 -- Enter Phase')
        print('4 -- Cash out entire Investment/Finish Game')
        print('5 -- View my Profile')
        print('6 -- Game Rules')
        print('7 -- Cryptocurrency information')
        print('Enter answer Below')
        ans1 = input()


        if ans1 == '1':
            optionBuy()
            continue

        elif ans1 == '2':
            optionSell()
            continue

        elif ans1 == '3':
            randomize()
            continue

        elif ans1 == '4':
            break

        elif ans1 == '5':
            getProfile()
            continue

        elif ans1 == '6':
            gameRules()
            continue

        elif ans1 == '7':
            cryptoInfo()

        elif ans1 == '':
            print('Please type one of the options listed.')
            print('')
            continue
        else:
            print('Please type a number from the listed options.')
            print('')
            continue
    cashOut()

            # sale all cryptos, and return profile
    # show beginning balance, ending balance, totalProfit, and summary

def gameRules():
    print('Game Rules')
    print('1: The goal is to end with a profit of at least 1 Million Dollars')
    print('2: You do have random debts that appear and take from you current balance.')
    print('3: If your debt is not able to be paid in full, stocks will be confiscated to make it possible.')
    print('Press enter for key information.')
    enter = input('')
    print('')
    print('Key Information')
    print('1: The option "Enter Phase" is when you fluctuate the stocks, generating rises and falls in stock prices.')
    print('2: Keep an eye on your current balance to make sure you can pay debts, You do not want your stocks taken.')
    print('3: Bitcoin is the leader, if it rises, they all rise, however, if it falls, chances of profit is rare but possible.')
    print('Press enter to continue with the game!')
    pressEnter = input('')



def game():
    global yourWallet
    print('Your Funds: '+ str(yourWallet))
    x = 0
    while x == 0:
        print('Have you played before? Y or N')
        response = input()
        response = response.lower()
        if response == 'n':
            print('We offer 5 cryptocurrencies: ' + str(listing))
            print('Here are the prices: ' + str(prices))
            print('Are you following everything? Yes(Y) or No(N) ')
            ans = input()
            ans = ans.lower()  # sends input to all lowercase
            if ans == 'y' or ans == 'yes':
                print('Good! your profile will appear like this:')
                getProfile()
                print('You should see your name and current balance of funds, it will update accordingly. Lets invest!')
                x+=1
                print('Press enter to continue.')
                forward1 = input()

            else:
                print('It is an investment game, we give you cash to invest, and you try your luck! Now, lets get started. Press enter to continue')
                hitEnter = input()
                print('Note: at any point of the game if you want to see your profile/wallet, just select the option: "My Profile"')
                print('It will appear like this:')
                getProfile()
                print('You should see your name and current balance of funds, it will update accordingly. Lets invest!')
                print('Press enter to begin playing!')
                forward = input()
                x+=1
            gameRules()


        elif response == 'y':
            print('Lets get started! Press enter to continue.')
            forward = input()
            x+=1
        else:
            print('Please type Y or N')
            continue
    print('')
    selectOption()


# calls the game method to run
# starting the game // Intro Code
print('What is your name? Type below.')
myName = input()
print('Welcome to the CryptoCurrency Simulator, ' +myName)
print('Are you familiar with investing? Y or N')
ans = input()
ans = ans.lower()
if ans == 'y' or ans == 'yes':
    print('Great! Lets get you some cash to get you started.')
else:
    print('No Worries! Investing is depositing your money into '
          'a certain product which can result in profit or losses overtime.')
    print('In this case, you will be choosing from a select list of cryptocurrency.')
    print('Lets get you started with some cash. Press enter to continue.')
    hitEnter = input()

game()





