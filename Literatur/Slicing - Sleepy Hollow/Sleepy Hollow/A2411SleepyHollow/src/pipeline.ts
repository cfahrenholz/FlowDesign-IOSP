function interaction() {
    const request = collect();
    const response = transform(request);
    project(response);
}

    function transform(request:any):any {
        const request1 = preProcess(request);
        const response1 = process(request1);
        return postProcess(response1);
    }

        function preProcess(request:any):any {
            const parsed = parse(request);
            const validated = validate(parsed);
            return map(validated);
        }

        function postProcess(response:any):any {
            const mapped = map(response);
            return format(mapped);
        }

        function process(request:any):any { 
            //...
        }



function run() { interaction(); }

function format(response:undefined):undefined{throw new Error();}

function parse(request:undefined):undefined {throw new Error();}
function validate(request:undefined):undefined {throw new Error();}
function map(request:undefined):undefined {throw new Error();}
function collect():undefined { throw new Error(); }
function project(response:undefined) {throw new Error; }