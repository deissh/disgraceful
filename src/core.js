const
  dictionary = require('./dictionary/main');

const
  LANGS = {
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
    var re = new RegExp(escapeRegExp(search), 'g');
    return str.replace(re, replacement);
}

function compile(text, lang) {
    /* text - текст для реплейса
     * lang - язык текста ('pon' or 'pas')
     */
    var commentRegExp = /((?:\/\*(?:[^*]|(?:\*+[^*\/]))*\*+\/)|(?:\/\/.*))/g;
    var tmpToken = 'pon_' + (new Date()).getTime() + '_';
    var rStringLiterals = {};
    text = text.replace(/\"(?:\\.|[^\"\\])*\"|\'(?:\\.|[^\'\\])*\'/g, function (val, pos) {
        var needKey = tmpToken + pos;
        rStringLiterals[needKey] = val;
        return needKey;
    });
    var commentsArray = text.match(commentRegExp) || [];
    text = iterateText(text, lang);
    // comeback comments
    text = text.replace(commentRegExp, function () {
        return commentsArray.shift();
    });
    // comeback strings
    for (tmpToken in rStringLiterals) {
        text = text.replace(tmpToken, rStringLiterals[tmpToken]);
    }
    // text = yoptTransliterateFunctionsNames(text);
    return text;
}


/**
 * @param text текст, по которому следует пройтись
 * @param to язык текста ('pon' or 'pas')
 */
function iterateText(text, to = 'pas') {
    let
      lang = LANGS[to];

    dictionary
        .sort((a, b) => {
            a = a[lang].length;
            b = b[lang].length;
            return b - a;
        })
        .forEach(pair => text = ReplaceAll(text, pair[lang], pair[+!lang]));

    return text;
}
