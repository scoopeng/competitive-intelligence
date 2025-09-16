#!/bin/bash
# Batch update script for 40 to 50 point conversion
# Created: January 2025

echo "=== Starting Batch Update to 50-point Scale ==="

# Create backup branch
echo "Creating backup branch..."
git checkout -b batch-update-50-point-$(date +%Y%m%d)
git commit -am "Checkpoint before batch 50-point update" || true

# Create score mapping file
echo "Creating score mappings..."
cat > /tmp/score_mappings.sed << 'EOF'
s/36\/40/38\/50/g
s/24\/40/29\/50/g
s/20\/40/25\/50/g
s/18\/40/23\/50/g
s/16\/40/20\/50/g
s/15\/40/18\/50/g
s/13\/40/17\/50/g
s/12\/40/15\/50/g
s/11\/40/13\/50/g
s/10\/40/12\/50/g
s/9\/40/11\/50/g
s/5\/40/6\/50/g
EOF

# Create category mapping file
echo "Creating category mappings..."
cat > /tmp/category_mappings.sed << 'EOF'
s/36-40 points/45-50 points/g
s/26-35 points/33-44 points/g
s/15-25 points/19-32 points/g
s/0-14 points/0-18 points/g
s/40 points maximum/50 points maximum/g
s/40 points max/50 points max/g
s/40-point/50-point/g
s/(40 BUPAF Score)/(50 BUPAF Score)/g
s/BUPAF Score: X\/40/BUPAF Score: X\/50/g
s/above 20\/40/above 25\/50/g
s/above 35\/40/above 44\/50/g
EOF

# Update category README files
echo "Updating category README files..."
for file in category-*/README.md; do
  if [ -f "$file" ]; then
    echo "  Updating $file"
    sed -i.bak -f /tmp/score_mappings.sed "$file"
    sed -i -f /tmp/category_mappings.sed "$file"
  fi
done

# Update framework files
echo "Updating framework files..."
for file in framework/*.md; do
  if [ -f "$file" ]; then
    echo "  Updating $file"
    sed -i.bak -f /tmp/score_mappings.sed "$file"
    sed -i -f /tmp/category_mappings.sed "$file"
  fi
done

# Update results files
echo "Updating results files..."
for file in results/*.md; do
  if [ -f "$file" ]; then
    echo "  Updating $file"
    sed -i.bak -f /tmp/score_mappings.sed "$file"
    sed -i -f /tmp/category_mappings.sed "$file"
  fi
done

# Archive old comprehensive analyses
echo "Archiving old comprehensive analyses..."
mkdir -p archive/old-40-point-analyses

# Move files but check they exist first
for pattern in "category-*/*/COMPREHENSIVE_BUPAF_ANALYSIS.md" "category-*/*/*bupaf*.md"; do
  for file in $pattern; do
    if [ -f "$file" ]; then
      echo "  Archiving $file"
      mv "$file" archive/old-40-point-analyses/ 2>/dev/null || true
    fi
  done
done

# Add archive header to moved files
echo "Adding archive headers..."
for file in archive/old-40-point-analyses/*.md; do
  if [ -f "$file" ]; then
    echo -e "# ⚠️ ARCHIVED DOCUMENT - USES OUTDATED 40-POINT SCORING\n\n$(cat $file)" > "$file"
  fi
done

# Clean up backup files
echo "Cleaning up backup files..."
find . -name "*.bak" -delete

# Commit changes
echo "Committing changes..."
git add -A
git status --short

echo ""
echo "=== Validation ==="
echo "40-point references remaining (excluding archive):"
grep -r "/40" . --include="*.md" --exclude-dir=archive 2>/dev/null | wc -l

echo ""
echo "38/50 references (Scoop's new score):"
grep -r "38/50" . --include="*.md" 2>/dev/null | wc -l

echo ""
echo "Files in archive:"
ls -la archive/old-40-point-analyses/ 2>/dev/null | wc -l

echo ""
echo "=== Batch Update Complete ==="
echo "Review changes with: git diff HEAD~1"
echo "Commit with: git commit -m 'Batch update: Convert all remaining files to 50-point scale'"