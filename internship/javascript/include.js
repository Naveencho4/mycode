
const btndisplaymodal=document.querySelector(".display-modal");
const modal=document.querySelector(".modal");
const blurr=document.querySelector(".try");
const btnclosemodal=document.querySelector(".close-modal");


const showmodla= function(){
    modal.classList.remove("hide");
    blurr.classList.add("blur");

}

const closemodla= function(){
    modal.classList.add("hide");
    blurr.classList.remove("blur");

}
btndisplaymodal.addEventListener("click" ,showmodla);
btnclosemodal.addEventListener("click" ,closemodla);
