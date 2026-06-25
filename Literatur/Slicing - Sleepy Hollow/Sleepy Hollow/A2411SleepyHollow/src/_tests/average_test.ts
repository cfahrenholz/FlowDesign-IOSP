import { assertEquals } from "https://deno.land/std@0.97.0/testing/asserts.ts";
import { CalcAverage } from "../average.ts";  // Pfad anpassen, falls nötig

Deno.test("CalcAverage - Normaler Fall mit positiven Zahlen", () => {
  const result = CalcAverage(["1", "2", "3", "4", "5"]);
  assertEquals(result, 3);
});

Deno.test("CalcAverage - Normaler Fall mit negativen und positiven Zahlen", () => {
  const result = CalcAverage(["-1", "0", "1"]);
  assertEquals(result, 0);
});

Deno.test("CalcAverage - Einzelne Zahl", () => {
  const result = CalcAverage(["10"]);
  assertEquals(result, 10);
});

Deno.test("CalcAverage - Dezimalzahlen", () => {
  const result = CalcAverage(["1.5", "2.5", "3.5"]);
  assertEquals(result, 2.5);
});

Deno.test("CalcAverage - Leeres Array", () => {
  const result = CalcAverage([]);
  assertEquals(result, NaN);
});


Deno.test("CalcAverage - Mischung aus gültigen und ungültigen Eingaben", () => {
  const result = CalcAverage(["1", "2", "drei", "4", "fünf"]);
  assertEquals(isNaN(result), true);
});