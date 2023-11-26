describe('Frontend Tests', () => {
  it('passes', () => {
    cy.visit('http://localhost:8000/')
    cy.visit('http://localhost:8000/contact')
    cy.get('p > .btn')
    cy.get('[href="mailto:here is your mail"]')
    cy.get('.navbar-toggler-icon').click()
    cy.get(':nth-child(1) > .nav-link').click()
    cy.get('.btn').click()
    cy.get('.text-center > :nth-child(1) > a').click()
    cy.visit('http://localhost:8000/')
  })
})