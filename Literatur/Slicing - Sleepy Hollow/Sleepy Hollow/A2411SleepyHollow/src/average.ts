class Head {
  constructor(private body:IBody){}

  async run() {
    const numbers = Deno.args.map(arg => Number(arg));

    const average = await this.body.calculate(numbers);

    console.log(`Durchschnitt: ${average.toFixed(2)}`);
  }
}

interface IBody {
  calculate(numbers:number[]):Promise<number>;
}

class HTTPBody implements IBody {
  private readonly url = "https://ralfw-whiteflea.web.val.run";

  async calculate(numbers: number[]): Promise<number> {
    const response = await fetch(this.url, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(numbers),
    });

    const result = await response.json();
    
    return result.average;
  }
}

const body = new HTTPBody();
const head = new Head(body);

await head.run();



