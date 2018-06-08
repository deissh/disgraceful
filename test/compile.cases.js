module.exports = [
  ['console.log();', 'красноглазое.чмо() нах'],
  ['checking', 'checking'],
  ['form', 'form'],
  ['settings', 'settings'],
  ['undefined', 'undefined'],
  ['upload', 'заебенить'],

  ['!x === y || z && a <= b++ ', 'чобляx блябуду y иличо z ичо a поц bплюсуюНа '],
  [
    '"чмо блябуду строка" === /** console.log() */ \'ичо\' // null changes in comments',
    '"чмо блябуду строка" блябуду /** console.log() */ \'ичо\' // null changes in comments'
  ]
];
