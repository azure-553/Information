"use client";

import { useState } from "react";

export default function Home() {
  const [question, setQuestion] = useState<string>("");

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setQuestion("");
  };

  return (
    <>
      <form>
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />
        <button type="submit">질문하기</button>
      </form>
    </>
  );
}
