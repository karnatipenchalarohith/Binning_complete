
from findInputBinsLminLmaxWminWmax import findInputBinsLminLmaxWminWmax as findInputBinsLminLmaxWminWmax
from findPointModelCardsLengthWidth import findPointModelCardsLengthWidth as findPointModelCardsLengthWidth
from RebinMatchingBinsToPointModelCard import RebinMatchingBinsToPointModelCard as RebinMatchingBinsToPointModelCard
from RebinPointModelToBinnedEquation import RebinPointModelToBinnedEquation as RebinPointModelToBinnedEquation
from RebinSameParameterDifferentParameter import RebinSameParameterDifferentParameter as RebinSameParameterDifferentParameter










wanttochange=1

if wanttochange==1:

    bins_array = findInputBinsLminLmaxWminWmax()

    point_model_cards = findPointModelCardsLengthWidth()

    print(bins_array)
    print(point_model_cards)

    matchBinsPointCards = RebinMatchingBinsToPointModelCard(bins_array, point_model_cards)

    print(matchBinsPointCards)

    FinalBinningEquation = RebinPointModelToBinnedEquation(matchBinsPointCards)

    print(FinalBinningEquation)

    RebinSameParameterDifferentParameter(matchBinsPointCards, FinalBinningEquation)


