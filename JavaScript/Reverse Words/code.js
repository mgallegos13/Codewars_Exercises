function reverseWords(str) {
  const strArr = str.split(' '); 
   for(let i = 0; i < strArr.length; i++){
      let list = strArr[i];
      strArr[i] = list
      .split('')
      .reverse()
      .join('');
   };
   return strArr.join(' ');
  
}


