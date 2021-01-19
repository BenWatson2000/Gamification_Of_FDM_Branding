const functions = require('./functions')

test ('returnIntTime', () => {
    expect(functions.returnIntTime('01:20')).toEqual(40);
})