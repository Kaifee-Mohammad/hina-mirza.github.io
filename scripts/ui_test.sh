#!/bin/bash
# Simple UI Test Script for Jekyll Site
# Tests UI after changes without requiring Python dependencies

BASE_URL="http://localhost:4000"
PASSED=0
FAILED=0
WARNINGS=0

echo "============================================================"
echo "UI Test Suite - $(date)"
echo "============================================================"
echo ""

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

pass_test() {
    echo -e "${GREEN}✓${NC} $1: $2"
    ((PASSED++))
}

fail_test() {
    echo -e "${RED}✗${NC} $1: $2"
    if [ -n "$3" ]; then
        echo "  Details: $3"
    fi
    ((FAILED++))
}

warn_test() {
    echo -e "${YELLOW}⚠${NC} $1: $2"
    ((WARNINGS++))
}

# Test 1: Server running
echo "Testing server status..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$BASE_URL")
if [ "$HTTP_CODE" = "200" ]; then
    pass_test "Server Status" "Server running at $BASE_URL"
else
    fail_test "Server Status" "Server returned $HTTP_CODE"
    exit 1
fi

echo ""

# Test 2: Homepage loads
echo "Testing Homepage..."
HOMEPAGE=$(curl -s "$BASE_URL/")
if [ -n "$HOMEPAGE" ]; then
    pass_test "Homepage Load" "Page loads successfully"

    # Count images
    IMG_COUNT=$(echo "$HOMEPAGE" | grep -o '<img[^>]*src="[^"]*"' | wc -l | tr -d ' ')
    if [ "$IMG_COUNT" -gt 0 ]; then
        pass_test "Homepage Images" "$IMG_COUNT images found in HTML"
    else
        warn_test "Homepage Images" "No images found"
    fi

    # Check for SVG images
    SVG_COUNT=$(echo "$HOMEPAGE" | grep -o 'src="[^"]*\.svg"' | wc -l | tr -d ' ')
    if [ "$SVG_COUNT" -gt 0 ]; then
        pass_test "Homepage SVG Images" "$SVG_COUNT SVG images found"
    else
        warn_test "Homepage SVG Images" "No SVG images found"
    fi

    # Check CSS
    CSS_COUNT=$(echo "$HOMEPAGE" | grep -o '<link[^>]*rel="stylesheet"' | wc -l | tr -d ' ')
    if [ "$CSS_COUNT" -gt 0 ]; then
        pass_test "Homepage CSS" "$CSS_COUNT stylesheets found"
    else
        fail_test "Homepage CSS" "No stylesheets found"
    fi

    # Check for lightbox
    if echo "$HOMEPAGE" | grep -q 'id="lightbox"'; then
        pass_test "Lightbox Elements" "Lightbox container found"
    else
        fail_test "Lightbox Elements" "Lightbox container not found"
    fi
else
    fail_test "Homepage Load" "Failed to load homepage"
fi

echo ""

# Test 3: Portfolio page
echo "Testing Portfolio page..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$BASE_URL/portfolio/")
if [ "$HTTP_CODE" = "200" ]; then
    pass_test "Portfolio Load" "Page loads successfully"
else
    fail_test "Portfolio Load" "Page returned $HTTP_CODE"
fi

# Test 4: Art Prints page
echo "Testing Art Prints page..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$BASE_URL/prints/")
if [ "$HTTP_CODE" = "200" ]; then
    pass_test "Art Prints Load" "Page loads successfully"
else
    fail_test "Art Prints Load" "Page returned $HTTP_CODE"
fi

# Test 5: About page
echo "Testing About page..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$BASE_URL/about/")
if [ "$HTTP_CODE" = "200" ]; then
    pass_test "About Load" "Page loads successfully"
else
    fail_test "About Load" "Page returned $HTTP_CODE"
fi

# Test 6: Contact page
echo "Testing Contact page..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$BASE_URL/contact/")
if [ "$HTTP_CODE" = "200" ]; then
    pass_test "Contact Load" "Page loads successfully"
else
    fail_test "Contact Load" "Page returned $HTTP_CODE"
fi

echo ""

# Test 7: Sample images
echo "Testing sample images..."
SAMPLE_IMAGES=(
    "/assets/images/portfolio/protea-sample.svg"
    "/assets/images/portfolio/fabric-sample.svg"
    "/assets/images/prints/protea-print.svg"
    "/assets/images/prints/floral-garden.svg"
    "/assets/images/prints/eucalyptus.svg"
)

for img in "${SAMPLE_IMAGES[@]}"; do
    HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$BASE_URL$img")
    if [ "$HTTP_CODE" = "200" ]; then
        pass_test "Image Test" "$img accessible"
    else
        fail_test "Image Test" "$img returned $HTTP_CODE"
    fi
done

echo ""

# Test 8: CSS file
echo "Testing CSS..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$BASE_URL/assets/css/main.css")
if [ "$HTTP_CODE" = "200" ]; then
    pass_test "CSS File" "Main stylesheet accessible"
else
    fail_test "CSS File" "Main stylesheet returned $HTTP_CODE"
fi

# Test 9: JavaScript file
echo "Testing JavaScript..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$BASE_URL/assets/js/main.js")
if [ "$HTTP_CODE" = "200" ]; then
    pass_test "JavaScript File" "Main script accessible"
else
    fail_test "JavaScript File" "Main script returned $HTTP_CODE"
fi

echo ""
echo "============================================================"
echo "Test Summary"
echo "============================================================"
echo -e "${GREEN}✓ Passed:  $PASSED${NC}"
echo -e "${RED}✗ Failed:  $FAILED${NC}"
echo -e "${YELLOW}⚠ Warnings: $WARNINGS${NC}"
echo "============================================================"
echo ""

if [ $FAILED -gt 0 ]; then
    echo "Some tests failed. Please review the output above."
    exit 1
else
    echo "All tests passed successfully!"
    exit 0
fi
