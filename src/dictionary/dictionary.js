var dictionary = [
    ["begin", " \\{ "],
    ["end", "\\}"]
];

dictionary.sort(function(a, b) {
    if (a[1].length < b[1].length){
        return 1;
    }
    else if (a[1].length > b[1].length) {
        return -1;
    } else {
        return 0;
    }
});
console.log(JSON.stringify(dictionary, null, '\t'));
