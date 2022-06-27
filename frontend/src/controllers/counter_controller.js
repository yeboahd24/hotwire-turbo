import {Controller} from '@hotwired/stimulus';
export default class extends Controller {
static values = {
count: { type: Number, default: 0 },
};
static targets = [
'count',
'initialDiv',
'progressDiv'
];
static classes = ['hidden'];
connect() {
this.countTarget.innerText = this.countValue;
}
countValueChanged(value, previousValue) {
console.log(`${previousValue} changed to ${value}`);
if (value === 1){
this.initialDivTarget.classList.add(this.hiddenClass);
this.progressDivTarget.classList.remove(this.hiddenClass);
}
}
increment(){
this.countValue++;
this.countTarget.innerText = this.countValue;
}
}