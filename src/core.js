const dictionary = require('./dictionary/main');

let LANGS = {
    pon: 0,
    pas: 1,
};

module.exports = {
    compile,
    dictionary,
};

function escapeRegExp(str) {
    str = str.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&');

    if (/^\w+$/.test(str)) {
        str = '\\b' + str + '\\b';
    }

    return str;
}

function ReplaceAll(str, search, replacement) {
    let re = new RegExp(escapeRegExp(search), 'g');
    return str.replace(re, replacement);
}

function compile(text, lang) {
    // lang - язык текста ('pon' or 'pas')
    let commentRegExp = /((?:\/\*(?:[^*]|(?:\*+[^*\/]))*\*+\/)|(?:\/\/.*))/g;
    let tmpToken = 'pon_' + (new Date()).getTime() + '_';
    let rStringLiterals = {};
    
    text = text.replace(/\"(?:\\.|[^\"\\])*\"|\'(?:\\.|[^\'\\])*\'/g, function (val, pos) {
        let needKey = tmpToken + pos;
        rStringLiterals[needKey] = val;
        return needKey;
    });
    let commentsArray = text.match(commentRegExp) || [];
    
    text = iterateText(text, lang);
    
    text = text.replace(commentRegExp, function () {
        return commentsArray.shift();
    });
    
    for (tmpToken in rStringLiterals) {
        text = text.replace(tmpToken, rStringLiterals[tmpToken]);
    }
    
    return text;
}

function iterateText(text, to = 'pas') {
    let lang = LANGS[to];

    dictionary
        .sort((a, b) => {
            a = a[lang].length;
            b = b[lang].length;
            return b - a;
        })
        .forEach(pair => text = ReplaceAll(text, pair[lang], pair[+!lang]));

    return text;
}
