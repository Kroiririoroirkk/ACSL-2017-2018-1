import sys

cardValues = {
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  'T': 10,
  'J': 11,
  'Q': 12,
  'K': 13,
  'A': 14
}

def processGame(line):
  params = line.strip().split(', ')
  pointTotal = int(params[0])
  hand = params[1:4]
  moves = params[4:]

  def processCard(card):
    return pointTotal + {
      '2': 2,
      '3': 3,
      '4': 4,
      '5': 5,
      '6': 6,
      '7': 7,
      '8': 8,
      '9': 0,
      'T': -10,
      'J': 11,
      'Q': 12,
      'K': 13,
      'A': 14 if pointTotal + 14 < 99 else 1}.get(card)
  
  def gameEnded():
    return pointTotal > 99
  
  def playerMove(move):
    nonlocal pointTotal
    maxCard = max(hand, key=cardValues.get)
    pointTotal = processCard(maxCard)
    hand.remove(maxCard)
    hand.append(moves[2*move])
    if gameEnded():
      return (pointTotal, 'dealer')
  
  def dealerMove(move):
    nonlocal pointTotal
    pointTotal = processCard(moves[2*move+1])
    if gameEnded():
      return (pointTotal, 'player')
  
  for move in range(3):
    playerMoveResult = playerMove(move)
    dealerMoveResult = dealerMove(move)
    if playerMoveResult:
      return playerMoveResult
    elif dealerMoveResult:
      return dealerMoveResult
  
  return playerMove(3)

for line in sys.stdin:
  total, winner = processGame(line)
  print(total, winner, sep=', ')
