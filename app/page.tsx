'use client'

import { useState } from 'react'

export default function Home() {
  const [question, setQuestion] = useState('')

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    setQuestion('')
  }

  return (
    <div>
      <h1 className="text-my-color">링클립</h1>
      <h1 className="text-3xl font-bold underline text-cyan-500">
        Hello world!
      </h1>
      <p>사용자 추가 색상</p>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={question}
          onChange={(e) => {
            setQuestion(e.target.value)
            console.log(e.target.value)
          }}
        />
        <button>질문하기</button>
      </form>
    </div>
  )
}
