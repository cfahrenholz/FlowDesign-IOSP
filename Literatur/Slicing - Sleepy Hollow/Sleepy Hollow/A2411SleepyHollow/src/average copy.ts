function calculateAverage(numbers: number[]): number {
  if (numbers.length === 0) {
    return 0;
  }
  const sum = numbers.reduce((acc, curr) => acc + curr, 0);
  return sum / numbers.length;
}

const numbers = Deno.args.map(arg => {
  return Number(arg);
});

const average = calculateAverage(numbers);

console.log(`Durchschnitt: ${average.toFixed(2)}`);