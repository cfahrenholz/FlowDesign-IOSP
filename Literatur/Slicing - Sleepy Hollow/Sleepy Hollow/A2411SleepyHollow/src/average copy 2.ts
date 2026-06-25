class Head {
  constructor(private body:IBody){}

  run() {
    const numbers = Deno.args.map(arg => Number(arg));

    const average = this.body.calculate(numbers);

    console.log(`Durchschnitt: ${average.toFixed(2)}`);
  }
}

interface IBody {
  calculate(numbers:number[]):number;
}

class AverageCalculationBody implements IBody {
  calculate(numbers: number[]): number {
    const sum = numbers.reduce((acc, curr) => acc + curr, 0);
    const average = sum / numbers.length;
  
    return average;
  }
}

const body = new AverageCalculationBody();
const head = new Head(body);

head.run();



