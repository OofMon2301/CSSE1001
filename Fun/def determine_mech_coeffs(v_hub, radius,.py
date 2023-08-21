def determine_mech_coeffs(v_hub, radius, omega, coeffs):
    # a_i is tuple of coefficients
    # rw is radius
    # v_hub is velocity
    # w is omega
    # k is number of coefficients
    # return the calculation
    fun = 0
    for i in range(len(coeffs)):
        fun += coeffs[i - 1] * (radius * omega / v_hub) ** i
        print(f"a_{i} = {coeffs[i]}")
    return fun


coeffs = (-2.57e-03, 2.311e-02, 2.155e-03, 3.703e-05, -1.367e-06)
print(determine_mech_coeffs(11.566, 40, 2.11, coeffs))
