import statistics

# Drug Pricing
weedOunce = 100
weedPen = 40
waxGram = 30
coke = 75
shroomOunce = 150
shroomHalf = 70
vape = 20

1 ##################
# How much is Currently in your Bank Account?
currentBank = 0

2 ##########################
# How Much Was Your Check?
checkValue = 0

bankTotal = checkValue + currentBank
print("Your Total Bank Balance is Now " + str(bankTotal))

3 ############################
# How Much Cash Do You Have?
currentCash = 0

4 #############################################
# How Much Cash Have You Made the Past 7 Days?
cashValues = [15, 18, 30, 8, 14, 19, 7]

dailyCash: int = statistics.mean(cashValues)
print("On Average, You Will Make $" + str(dailyCash) + " Per Day in Cash")

5 ##############################################
# How Many **WORK** Days Until You Get Your Next PayCheck?
daysTill = 0

gainedCash = daysTill * dailyCash
cashTotal = gainedCash + currentCash
print ("Meaning by your next paycheck, you would have made approximatly $" + str(gainedCash) + " In Cash")

6 ############################################
# How Much Do You Want to Spend on Essenitals?
essenSpend = 0

bankAfterEssen = bankTotal - essenSpend
print("After Purchasing The Essentials, Your Remaning Balance Would Be: $" + str(bankAfterEssen))

7 ##############################
# List Online Memnships
onlineMemb = 20 + 20 + 10

bankAfterMembs = bankAfterEssen - onlineMemb
print("After The Online Memberships That Always Charge at the Worst Time, Your Total Becomes: $" + str(bankAfterMembs))

8 ###################################
# How Much Money Do You Want to Save?
saveMoney = 0

bankAfterSave = bankAfterMembs - saveMoney
print("If you were to save $" + str(saveMoney) + " Your Remaining Balance Would Be: $" + str(bankAfterSave))

9 #####################################
# Now Finally...What Drugs Do You Want?

weedOzAmm = 0
weedPenAmm = 0
waxAmm = 0
cokeAmm = 0
shroomOzAmm = 0
shroomHalfAmm = 0 
vapeAmm = 0

callWeedOz = weedOzAmm   
callPen = weedPenAmm
callWax = waxAmm
callCoke = cokeAmm
callShroomOz = shroomOzAmm
callShroomHalf = shroomHalfAmm
callVape = vapeAmm

weedCharge = weedOzAmm * weedOunce
penCharge = weedPenAmm * weedPen
waxCharge = waxAmm * waxGram
cokeCharge = cokeAmm * coke
shroomOzCharge = shroomOzAmm * shroomOunce
shroomHalfCharge= shroomHalfAmm * shroomHalf
vapeCharge = vapeAmm * vape

totalCharge = weedCharge + penCharge + waxCharge + cokeCharge + shroomOzCharge + shroomHalfCharge + vapeCharge

afterDrugCharge = bankAfterSave - totalCharge
afterDrugChargeWCash = afterDrugCharge + cashTotal

print("You Have Selected: " + str(callWeedOz) + " Oz of Weed, " + str(callCoke) + " Gram(s) of Coke, " + str(shroomOzAmm) + " Oz of Shrooms, " + str(shroomHalfAmm) + " 1/2 Oz of Shrooms, " + str(vapeAmm) + " Vape(s), " + str(callPen) + " Weed Pen(s), and " + str(callWax) + " gram(s) of Wax")
print("This will leave you withhhh....$" + str(afterDrugCharge) + " to Spend on Whatever You Want!")
print("And If You Include Your Current Cash + Cash Flow, $" + str(afterDrugChargeWCash) + " Would Be Your Remaining Spends")