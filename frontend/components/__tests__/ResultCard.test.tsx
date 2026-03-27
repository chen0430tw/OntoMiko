/**
 * ResultCard component tests
 */

import { render, screen } from '@testing-library/react'
import ResultCard, { DivineResult } from '../ResultCard'

describe('ResultCard', () => {
  const mockResult: DivineResult = {
    category: '宇宙同意',
    state: 'qY',
    reason: '设想具有来源、承载、可判性与可接受代价',
    permission_score: 0.91,
    note: '需要高权限',
  }

  it('renders nothing when result is null', () => {
    const { container } = render(<ResultCard result={null} />)
    expect(container.firstChild).toBeNull()
  })

  it('renders category', () => {
    render(<ResultCard result={mockResult} />)
    expect(screen.getByText('宇宙同意')).toBeInTheDocument()
  })

  it('renders state', () => {
    render(<ResultCard result={mockResult} />)
    expect(screen.getByText(/终态：qY/)).toBeInTheDocument()
  })

  it('renders reason', () => {
    render(<ResultCard result={mockResult} />)
    expect(screen.getByText(mockResult.reason)).toBeInTheDocument()
  })

  it('renders permission score when present', () => {
    render(<ResultCard result={mockResult} />)
    expect(screen.getByText(/许可度：91.0%/)).toBeInTheDocument()
  })

  it('renders note when present', () => {
    render(<ResultCard result={mockResult} />)
    expect(screen.getByText(/OntoMiko 备注：需要高权限/)).toBeInTheDocument()
  })

  it('renders without permission score', () => {
    const resultWithoutScore: DivineResult = {
      category: '宇宙不同意',
      state: 'qN',
      reason: '来源不足',
    }
    render(<ResultCard result={resultWithoutScore} />)
    expect(screen.queryByText(/许可度：/)).not.toBeInTheDocument()
  })
})
