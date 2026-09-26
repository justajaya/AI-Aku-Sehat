# Aku Sehat AI — Revision Notes

This revision is based on the uploaded FINAL-CLEAN project; the existing application structure, Supabase flow, food-image AI analysis, dataset matching, dashboard, logging, and what-if simulation are retained.

## Main revision
- Fixed the recommendation workflow so multiple preferences such as `ayam, nasi, telur` are treated as separate terms instead of one literal dataset query.
- If a preference has no direct match, the app no longer stops with an empty recommendation; it falls back to the broader validated nutrition catalog.
- Added an AI recommendation layer using the existing Gemini helper.
- AI receives only validated candidate foods and program-calculated nutrition values. It selects/combines candidates and explains the recommendation.
- Added meal calorie limit and stronger UI explanation of the AI/data separation.
- Existing image-analysis and exact-match nutrition resolution are preserved.

## Security
The uploaded `.env` is intentionally not included in the revised ZIP. Copy your existing local `.env` values or use `.env.example`.
