const functions = require('./cablefunctions')
  test('shuffle', () => {
    const array = [ 1,2,3,4,5]
      expect(array).toContain(1)
      expect(array).toContain(2)
      expect(array).toContain(3)
      expect(array).toContain(4)
      expect(array).toContain(5)
      expect(array.length).toEqual(5)


  })
test ('formatTime', () => {
    expect(functions.formatTime('100')).toEqual('1:40');
})
test ('lineBreak with short string', () => {
    expect(functions.lineBreak('Hello')).toEqual('Hello');
})
test ('lineBreak with long string', () => {
    //const output =
   // expect(functions.lineBreak('Hello')).toEqual('Hello');
})