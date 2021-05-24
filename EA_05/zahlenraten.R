TRIES <- 3
won <- FALSE

readnum <- function(){
  guess <- readline('Your guess: ')
  guess <- as.integer(guess)
  return(guess)
}

x <- round(runif(1, -0.49 ,10.49), 0)

for (n in seq.int(1, TRIES)){
  guess <- readnum()
  if (guess == x) {
    won <- TRUE
    break
  }
}

if (won == TRUE) {
  print('You win!')
} else {
  print('You loose :(')
}