type CallBackError = Error | null;
type CallBack = (error: CallBackError, response: Object) => void;
type SendRequest = (cb: CallBack) => void;

function sendRequest(cb: CallBack): void {
    if(cb){
        cb(null, { message: 'todo salio como lo planeamos'});
    }
}

const sendRequest2: SendRequest = (cb: CallBack): void => {
    if(cb){
        cb(null, { message: 'todo salio como lo planeamos'});
    }
}