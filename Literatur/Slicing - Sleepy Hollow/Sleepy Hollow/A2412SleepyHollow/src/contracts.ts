type SessionID = string;
type Description = string;
type Item = string;

interface IPOProcessor {
  // Start method
  start(sessionID: SessionID): Promise<{
    description: Description;
    items: Item[];
  }>;

  // Publish method
  publish(description:string, items:Item[]): Promise<{
    sessionID: SessionID;
  }>;

  // Update method
  update(): Promise<{
    items: Item[];
  }>;
}

interface ICrowdProcessor {
  // Start method
  start(sessionID: SessionID): Promise<{
    description: Description;
    items: Array<{
      index: number;
      title: string;
    }>;
  }>;

  // Submit method
  submit(indexes: number[]): Promise<void>;
}
