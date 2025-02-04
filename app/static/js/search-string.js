
let scopelistopened = false

let CurrentScope = document.querySelector('.CurrentScope .text');
let ScopeList = document.querySelector('.ScopeList');


let RealSelector = document.querySelector('#scope');
let RealScopeList = RealSelector.querySelectorAll('option');

let Arrow = document.querySelector('.CurrentScope .arrow');


let ValueByName = {};

let current_value = RealSelector.value;

console.log('--->', current_value)

for (let scope = 0; scope < RealScopeList.length; scope++) {

  let name = RealScopeList[scope].innerText
  ValueByName[name] = RealScopeList[scope].value


  let copyScope = document.createElement('div')
  copyScope.classList.add('Scope')


  copyScope.addEventListener("click", SelectScope, false)

  copyScopeText = document.createElement('div')
  copyScopeText.classList.add('checkbox')
  copyScope.append(copyScopeText)

  copyScopeText = document.createElement('div')
  copyScopeText.classList.add('text')
  copyScopeText.textContent = name
  copyScope.append(copyScopeText)

  if (scope == 0){
    copyScope.classList.add('check');
    CurrentScope.textContent = name
  };

  ScopeList.append(copyScope)
}



function ShowCloseScopeList () {

  if (scopelistopened) {
    Arrow.style.transform = 'rotate(0deg)';
    ScopeList.style.display = 'none'
    scopelistopened = false
  }
  else {
    Arrow.style.transform = 'rotate(180deg)';
    ScopeList.style.display = 'grid'
    scopelistopened = true
  }
}


function SelectScope () {

  name = this.innerText
  value = ValueByName[name]


  if (CurrentScope.textContent != name){
    ScopeList.querySelector('.check').classList.remove('check')

    RealSelector.value = value;
    this.classList.add('check');
    CurrentScope.textContent = name;
  }

  ShowCloseScopeList();
}




