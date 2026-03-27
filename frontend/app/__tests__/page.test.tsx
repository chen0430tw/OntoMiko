/**
 * HomePage component tests
 */

import { render, screen, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import HomePage from '../page'

// Mock the API
global.fetch = jest.fn()

describe('HomePage', () => {
  beforeEach(() => {
    jest.clearAllMocks()
  })

  it('renders title and description', () => {
    render(<HomePage />)
    expect(screen.getByText('宇宙许可占卜姬')).toBeInTheDocument()
    expect(screen.getByText(/把你的天马行空交给宇宙审核/)).toBeInTheDocument()
  })

  it('renders textarea and submit button', () => {
    render(<HomePage />)
    expect(screen.getByRole('textbox')).toBeInTheDocument()
    expect(screen.getByRole('button', { name: '开始占验' })).toBeInTheDocument()
  })

  it('disables submit button when text is empty', () => {
    render(<HomePage />)
    const button = screen.getByRole('button', { name: '开始占验' })
    expect(button).toBeDisabled()
  })

  it('enables submit button when text is entered', async () => {
    render(<HomePage />)
    const textarea = screen.getByRole('textbox')
    const button = screen.getByRole('button', { name: '开始占验' })

    await userEvent.type(textarea, '测试文本')

    waitFor(() => {
      expect(button).not.toBeDisabled()
    })
  })

  it('shows loading state during submission', async () => {
    const mockPromise = new Promise(() => {}) // Never resolves
    ;(global.fetch as jest.Mock).mockImplementationOnce(() => mockPromise)

    render(<HomePage />)
    const textarea = screen.getByRole('textbox')
    const button = screen.getByRole('button', { name: '开始占验' })

    await userEvent.type(textarea, '测试文本')
    await userEvent.click(button)

    expect(screen.getByText('占验中...')).toBeInTheDocument()
  })

  it('displays result card on successful API call', async () => {
    const mockResult = {
      category: '宇宙同意',
      state: 'qY',
      reason: '测试通过',
      permission_score: 0.85,
    }

    ;(global.fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      json: async () => mockResult,
    })

    render(<HomePage />)
    const textarea = screen.getByRole('textbox')
    const button = screen.getByRole('button', { name: '开始占验' })

    await userEvent.type(textarea, '测试文本')
    await userEvent.click(button)

    await waitFor(() => {
      expect(screen.getByText('宇宙同意')).toBeInTheDocument()
    })
  })

  it('handles API error gracefully', async () => {
    ;(global.fetch as jest.Mock).mockRejectedValueOnce(new Error('Network error'))

    render(<HomePage />)
    const textarea = screen.getByRole('textbox')
    const button = screen.getByRole('button', { name: '开始占验' })

    await userEvent.type(textarea, '测试文本')
    await userEvent.click(button)

    await waitFor(() => {
      expect(screen.getByText('系统异常')).toBeInTheDocument()
    })
  })
})
